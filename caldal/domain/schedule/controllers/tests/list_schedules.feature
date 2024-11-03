Feature: 스케쥴 목록 가져오기
  스케쥴 목록 가져오는 API를 테스트합니다.

  Background:
    Given 이메일이 "a@gmail.com"인 사용자가 "GOOGLE" 로그인으로 회원가입했습니다.

  Scenario: 생성한 스케쥴이 없을 경우
    When 이메일이 "a@gmail.com"인 사용자가 시간대 "Asia/Seoul"의 "2024-10-01"부터 "2024-10-31"까지의 스케쥴 목록을 요청합니다.
    Then 서버의 응답 상태코드는 200입니다.
    And 응답 결과는 다음과 같습니다.
      """
      []
      """

  Scenario: 스케쥴을 생성했고, 스케쥴이 생성된 시간을 포함하는 시간 필터를 요청한 경우
    Given 이메일이 "a@gmail.com"인 사용자가 다음과 같이 일정을 생성했습니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-01T01:00:00+09:00"
      }
      """
    When 이메일이 "a@gmail.com"인 사용자가 시간대 "Asia/Seoul"의 "2024-10-01"부터 "2024-10-31"까지의 스케쥴 목록을 요청합니다.
    Then 서버의 응답 상태코드는 200입니다.
    And 응답 결과는 다음과 같습니다.
      """
      [
        {
          "title": "개발 공부",
          "content": "Python 공부",
          "start_time": "2024-10-01T00:00:00+09:00",
          "end_time": "2024-10-01T01:00:00+09:00"
        }
      ]
      """