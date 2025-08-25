import json

def read_csv_file(filename):
    """CSV 파일을 읽어서 리스트로 반환"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # 헤더와 데이터 분리
        header = lines[0].strip().split(',')
        data = []
        
        for line in lines[1:]:
            if line.strip():  # 빈 줄 제외
                row = line.strip().split(',')
                data.append(row)
        
        print(f'파일 "{filename}" 읽기 완료')
        print(f'총 {len(data)}개의 로그 항목 발견\n')
        
        return header, data
    
    except FileNotFoundError:
        print(f'오류: "{filename}" 파일을 찾을 수 없습니다.')
        return None, None
    except Exception as e:
        print(f'파일 읽기 오류: {e}')
        return None, None

def print_list_data(header, data):
    """리스트 데이터를 화면에 출력"""
    print('=== 로그 데이터 출력 ===')
    print(f'{header[0]:<12} | {header[1]:<20} | {header[2]}')
    print('-' * 60)
    
    for row in data:
        if len(row) >= 3:
            print(f'{row[0]:<12} | {row[1]:<20} | {row[2]}')
    print()

def sort_by_time_reverse(data):
    """시간 역순으로 정렬"""
    try:
        # timestamp 기준으로 역순 정렬
        sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
        print('시간 역순으로 정렬 완료\n')
        return sorted_data
    except Exception as e:
        print(f'정렬 오류: {e}')
        return data

def convert_to_dict(header, data):
    """리스트를 사전 객체로 변환"""
    dict_data = []
    
    for row in data:
        if len(row) >= 3:
            row_dict = {
                header[0]: row[0],
                header[1]: row[1], 
                header[2]: row[2]
            }
            dict_data.append(row_dict)
    
    print(f'사전 객체로 변환 완료 ({len(dict_data)}개 항목)\n')
    return dict_data

def save_to_json(data, filename):
    """사전 객체를 JSON 파일로 저장"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        
        print(f'JSON 파일 "{filename}" 저장 완료\n')
        return True
    
    except Exception as e:
        print(f'JSON 파일 저장 오류: {e}')
        return False

# 보너스 기능 제거됨

def main():
    """메인 실행 함수"""
    input_filename = 'mission_computer_main.log'
    output_filename = 'mission_computer_main.json'
    
    print('화성 미션 컴퓨터 로그 분석 시스템')
    print('=' * 50)
    
    # 1. CSV 파일 읽기
    header, data = read_csv_file(input_filename)
    if data is None:
        print('프로그램을 종료합니다.')
        return
    
    # 2. 리스트 객체 출력
    print_list_data(header, data)
    
    # 3. 시간 역순으로 정렬
    sorted_data = sort_by_time_reverse(data)
    
    print('=== 시간 역순 정렬 결과 ===')
    print_list_data(header, sorted_data[:5])  # 처음 5개만 출력
    
    # 4. 사전 객체로 변환
    dict_data = convert_to_dict(header, sorted_data)
    
    # 5. JSON 파일로 저장
    if save_to_json(dict_data, output_filename):
        print('모든 작업이 성공적으로 완료되었습니다!')
    
    # 보너스: 특정 문자열 검색
    print('\n=== 보너스 과제: 로그 검색 ===')
    search_term = input('검색할 문자열을 입력하세요 (예: Oxygen): ').strip()
    
    if search_term:
        search_results = search_logs(dict_data, search_term)
        if not search_results:
            print('검색 결과가 없습니다.')

if __name__ == '__main__':
    main()
