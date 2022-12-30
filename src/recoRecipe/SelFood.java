package recoRecipe;

import java.util.*;
import java.util.stream.IntStream;

public class SelFood {

	/*
	 * array()를 사용하여 마지막 요소를 제거 후 배열 return a : 선택된 배열 리스트 index : 선택된 배열의 음식 인덱스 값
	 */
	private static String[] remove(String[] a, int index) {

		if (a == null || index < 0 || index >= a.length) {
			return a;
		}

//		String[] result = new String[a.length - 1];
//		System.out.println("size : " + a.length + " | " + result.length + " | " + index);
		/*
		 * IntStream.range(0부터 원본 배열의 길이만큼 값 생성)
		 * filter 메서드. 특정 인덱스(선택된 음식의 배열 인덱스 값)가 아닌(뺀) 값(idx != index)을 반환
		 * mapToObj(특정 인덱스 요소를 제외한 배열의 요소 할당)
		 * 스트림 결과를 배열로 반환
		 * */
		String[] result = IntStream.range(0,  a.length)
						  .filter(idx -> idx != index)
						  .mapToObj(idx -> a[idx])
						  .toArray(String[]::new);
		return result;
	}

	public void sFood(int lastDate, int lastDay) {
		/*
		 * 음식 카테고리 배열 
		 * foodList[0] : 한식 
		 * foodList[1] : 중식 
		 * foodList[2] : 일식 
		 * foodList[3] : 양식
		 * foodList[4] : 기타
		 */
		String foodList[][] = {
				{ "카레라이스", "육회", "돈까스", "보쌈정식", "김치볶음밥", "돼지국밥", "뼈해장국", "순대국밥", "김치찌개", "된장찌개", "갈비찜", "낙지볶음", "닭볶음탕",
				  "수육", "오징어볶음", "찜닭", "떡만둣국", "부대찌개", "비빔국수", "냉면", "막국수", "잔치국수", "비빔밥", "칼국수", "떡볶이", "족발",
				  "샤브샤브", "생선구이", "곱창전골", "새로운 집", "제육볶음", "돌솥제육비빔밥", "뚝배기불고기", "청국장", "해물라면", "평양냉면" },
				{ "마라탕", "마라샹궈", "중화볶음밥", "짜장면", "짬뽕", "탕수육", "새로운 집", "잡채밥", "상해루"},
				{ "초밥", "메밀국수", "우동", "새로운 집", "돈부리", "소바", "매운라멘", "라멘", "돈카츠", "가츠우동나베", "튀김덮밥"},
				{ "누룽지삼계국물파스타", "봉골레파스타", "베이컨크림파스타", "맥도날드", "버거킹", "피자", "스테이크", "새로운 집", "오므라이스", "로제파스타", 
				  "크림리조또", "리조또" },
				{ "쌀국수", "새로운 집", "곱창쌀국수", "뼈쌀국수", "스테이크덮밥", "나시고랭", "맹그로브", "탕탕"} };

		Random rand = new Random();
		List<String> list = Arrays.asList("한식", "중식", "일식", "양식", "기타");
		// compareK : 키 비교(이전 값 저장) storeK : 현재 값 저장
		String compareK = "";
		String storeK = "";

		/*
		 * 음식 카테고리 list 랜덤 
		 * randL : 리스트 중 랜덤 
		 * randI : 선택된 랜덤 요리의 인덱스 
		 * flag : 음식 카테고리 재선택 체크
		 * count : 음식 카테고리 내 인덱스 모두 소진 시 count(*삭제)
		 * randL2 : 랜덤으로 선택된 원소의 원래 index 값(*삭제)
		 * randS : index에 해당하는 원소(문자열) 
		 * randF : 해당 카테고리의 랜덤 메뉴 값 
		 * listR : 선택된 카테고리의 음식 배열(*삭제)
		 */
		int randL = 0;
		int randI = 0;
		int flag = 0;
		String randS = "";
		String randF = "";
		/* 카테고리 내 메뉴 개수가 적으면 중복해서 뜨는 경우가 있음. */
		String randList[] = new String[lastDate];

		// 말일에 대한 식단 출력
		for (int i = 0; i < lastDate; i++) {
			flag = 0;
			while (flag < 1) {
				// 해당 카테고리의 랜덤 메뉴 원소
				randL = rand.nextInt(list.size());
				// 만약, 음식 카테고리의 음식 모두 소진 시, 발생하는 bound error 해결
				if (foodList[randL].length == 0) {
					continue;
				} else {
					randI = rand.nextInt(foodList[randL].length);
					flag = 1;
				}
			}
			
			randS = list.get(randL);
			storeK = randS;
			if (i == 0) {
				// 다음에 비교할 값 = 현재 값
				compareK = storeK;
				// foodList[랜덤으로 선택된 음식 카테고리][해당 종류의 랜덤 음식]
				randF = foodList[randL][randI];
				randList[i] = randF;
				foodList[randL] = remove(foodList[randL], randI);
				System.out.println("0" + (i + 1) + "일 : " + storeK + " | " + randF);
			} else {
				// 메뉴 중복 제거
				for (int j = 0; j <= i; j++) {
					if (storeK != compareK) {
						// foodList[랜덤으로 선택된 음식 카테고리][해당 카테고리의 랜덤 음식]
						randF = foodList[randL][randI];
						randList[i] = randF;
						if (randList[j] == null && randList[i] == randList[j]) {
							--i;
							break;
						} else {
							foodList[randL] = remove(foodList[randL], randI);
							if (i < 9) {
								System.out.println("0" + (i + 1) + "일 : " + storeK + " | " + randF);
							} else {
								System.out.println((i + 1) + "일 : " + storeK + " | " + randF);
							}
							// 다음에 비교할 값 = 현재 값
							compareK = storeK;
							break;
						}
					} else {
						--i;
						break;
					}
				}
			}
		}
		// System.out.println("\n" + lastDay + "일 오늘의 식단은 [" + randList[lastDay - 1] + "] 입니다.");
	}
}