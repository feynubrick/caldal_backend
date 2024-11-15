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
        "end_time": "2024-10-01T01:00:00+09:00",
        "is_all_day": false
      }
      """
    Then 서버의 응답 상태코드는 201입니다.
    And 응답된 일정 데이터는 다음과 같습니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-01T01:00:00+09:00",
        "is_all_day": false,
        "timezone": "Asia/Seoul"
      }
      """
    And 다음 조건과 일치하는 이메일이 "a@gmail.com"인 사용자의 일정이 1개 존재합니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-01T01:00:00+09:00",
        "is_all_day": false
      }
      """

  Scenario: 사용자는 한국이 아닌 다른 시간대에서도 일정을 생성할 수 있다.
    When 이메일이 "a@gmail.com"인 사용자가 다음과 같이 일정 생성을 요청합니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T00:00:00+00:00",
        "end_time": "2024-10-01T01:00:00+00:00",
        "is_all_day": false,
        "timezone": "Europe/London"
      }
      """
    Then 서버의 응답 상태코드는 201입니다.
    And 응답된 일정 데이터는 다음과 같습니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T00:00:00+00:00",
        "end_time": "2024-10-01T01:00:00+00:00",
        "is_all_day": false,
        "timezone": "Europe/London"
      }
      """
    And 다음 조건과 일치하는 이메일이 "a@gmail.com"인 사용자의 일정이 1개 존재합니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T00:00:00+00:00",
        "end_time": "2024-10-01T01:00:00+00:00",
        "is_all_day": false,
        "timezone": "Europe/London"
      }
      """

  Scenario: 사용자는 종일 일정을 생성할 수 있다.
    When 이메일이 "a@gmail.com"인 사용자가 다음과 같이 일정 생성을 요청합니다.
      """
      {
        "title": "엄마 생신",
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-02T00:00:00+09:00",
        "is_all_day": true
      }
      """
    Then 서버의 응답 상태코드는 201입니다.
    And 응답된 일정 데이터는 다음과 같습니다.
      """
      {
        "title": "엄마 생신",
        "content": null,
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-02T00:00:00+09:00",
        "is_all_day": true,
        "timezone": "Asia/Seoul"
      }
      """
    And 다음 조건과 일치하는 이메일이 "a@gmail.com"인 사용자의 일정이 1개 존재합니다.
      """
      {
        "title": "엄마 생신",
        "content": null,
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-02T00:00:00+09:00",
        "is_all_day": true,
        "timezone": "Asia/Seoul"
      }
      """

  Scenario: 종일 일정 생성을 요청할 때 해당 날의 시작 시간과 다음 날의 시작시간을 보내야 한다.
    When 이메일이 "a@gmail.com"인 사용자가 다음과 같이 일정 생성을 요청합니다.
      """
      {
        "title": "엄마 생신",
        "start_time": "2024-10-01T00:00:00+09:00",
        "end_time": "2024-10-01T23:59:59.999+09:00",
        "is_all_day": true
      }
      """
    Then 서버의 응답 상태코드는 400입니다.

  Scenario: 시작 시간은 종료 시간보다 미래일 수 없다.
    When 이메일이 "a@gmail.com"인 사용자가 다음과 같이 일정 생성을 요청합니다.
      """
      {
        "title": "개발 공부",
        "content": "Python 공부",
        "start_time": "2024-10-01T01:00:01+09:00",
        "end_time": "2024-10-01T01:00:00+09:00"
      }
      """
    Then 서버의 응답 상태코드는 400입니다.
