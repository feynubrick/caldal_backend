Feature: 스케쥴 생성하기
  사용자가 스케쥴을 생성할 때 사용하는 API의 테스트

  Background:
    Given 이메일이 "a@gmail.com"인 사용자가 "GOOGLE" 로그인으로 회원가입했습니다.

  Scenario: 사용자는 일정을 생성할 수 있다.
    When 이메일이 "a@gmail.com"인 사용자가 다음과 같이 일정 생성을 요청합니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-01T01:00:00+09:00"
      }
      """
    Then 서버의 응답 상태코드는 201입니다.
    And 다음 조건과 일치하는 이메일이 "a@gmail.com"인 사용자의 일정이 1개 존재합니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-01T01:00:00+09:00"
      }
      """
    And 응답된 일정 데이터는 다음과 같습니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-01T01:00:00+09:00"
      }
      """
