package recoRecipe;

public class Main {
	public static void main(String[] args) {

		CalendarF cal = new CalendarF();
        int lastDate = cal.cFood();

        // lastDay : 연도, 월 입력으로 오늘의 식단 사용X
        int lastDay = cal.dFood();

        // 해당월 말일에 맞는 음식 종류 랜덤 출력
        SelFood sfd = new SelFood();
        sfd.sFood(lastDate, lastDay);
	}
}
