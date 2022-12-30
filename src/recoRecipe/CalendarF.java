package recoRecipe;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Scanner;

public class CalendarF {
	
	Calendar fc = Calendar.getInstance();
	SimpleDateFormat fCal = new SimpleDateFormat();
	String formatYear = "yyyy";
	String formatMonth = "MM";
	String formatDay = "d";

	public int cFood(){
		// 연도, 달 입력
		Scanner dt = new Scanner(System.in);
		int inYear = 0, inMonth = 0, month = 0, comYear = 0;
		String year = "";

		System.out.println("연도에 00을 입력하시면 이번 달 식단표가 출력됩니다.");
		System.out.print("원하는 연도 : ");
		year = dt.nextLine();
		comYear = Integer.parseInt(year);

		if (year.equals("00")){
			fCal.applyPattern(formatYear);
			inYear = Integer.parseInt(fCal.format(fc.getTime()));
			fCal.applyPattern(formatMonth);
			inMonth = Integer.parseInt(fCal.format(fc.getTime()));
		}
		else {
			while (comYear < 1900 || comYear > 9999 || year.length() != 4) {
				System.out.print("원하는 연도 : ");
				year = dt.nextLine();
				comYear = Integer.parseInt(year);
			}
			System.out.print("원하는 달 : ");
			month = dt.nextInt();

			while(month == 0 || month >= 13){
				System.out.print("원하는 달 : ");
				month = dt.nextInt();
			}
			inYear = Integer.parseInt(year);
			inMonth = month;
		}

		System.out.println("**********************");
		System.out.println("   " + inYear + "년 " + inMonth + "월 식단표");
		System.out.println("**********************");

		// 입력받거나 기본 값(올해 달) 세팅 > 말일 구하기(월-1 : 입력 월)
		fc.set(inYear, inMonth-1, 1);
//		System.out.println("lastDate : " + lastDate);

		return fc.getActualMaximum(Calendar.DAY_OF_MONTH);
	}
	//오늘의 식단 (연도, 월 입력으로 사용X)
	public int dFood() {
		fCal.applyPattern(formatDay);
		return Integer.parseInt(fCal.format(fc.getTime()));
	}
}
