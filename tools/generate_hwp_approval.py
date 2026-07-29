from pathlib import Path
import hwpers

OUT = Path("generated/사업수행계획서_변경승인서.hwp")
OUT.parent.mkdir(parents=True, exist_ok=True)

w = hwpers.HwpWriter()
w.set_title("사업수행계획서 변경승인서")
w.set_subject("정보화사업 사업수행계획서 변경 승인")
w.set_author("발주기관")
w.set_company("발주기관")
w.set_a4_portrait()
w.set_page_margins_mm(18.0, 18.0, 18.0, 18.0)

# 제목
w.add_paragraph("")
w.add_aligned_paragraph("변  경  승  인  서", hwpers.ParagraphAlignment.Center)
w.add_paragraph("")

# 기본정보
basic = hwpers.TableBuilder(5, 4)
rows = [
    ["사 업 명", "[사업명 입력]", "용역책임자", "[성명 입력]"],
    ["추진단계명", "설계 단계", "변경요청번호", "[번호 입력]"],
    ["제    목", "사업수행계획서 변경 승인", "변경승인번호", "[번호 입력]"],
    ["변경요청일", "2026년   월   일", "변경승인일", "2026년   월   일"],
    ["검토부서", "[부서명 입력]", "검 토 자", "[성명 입력]"],
]
for r, row in enumerate(rows):
    for c, text in enumerate(row):
        basic.set_cell(r, c, text)
basic.set_all_borders(hwpers.CellBorderStyle())
w.add_table_with_builder(basic)

w.add_paragraph("")

# 변경유형
w.add_paragraph_with_bold("[변경유형]")
change_type = hwpers.TableBuilder(4, 2)
change_rows = [
    ["개 발", "□ 기능요구   □ 성능요구   □ 품질요구   □ 기타(             )"],
    ["장 비", "□ 해당   □ 해당 없음"],
    ["인 력", "□ 해당   □ 해당 없음"],
    ["기 타", "□ (                                                        )"],
]
for r, row in enumerate(change_rows):
    for c, text in enumerate(row):
        change_type.set_cell(r, c, text)
change_type.set_all_borders(hwpers.CellBorderStyle())
w.add_table_with_builder(change_type)

w.add_paragraph("")

# 승인 개요
w.add_paragraph_with_bold("[변경승인내용]")
w.add_paragraph(
    "귀 사가 제출한 사업수행계획서 변경요청서(변경요청번호: [          ])에 대하여 "
    "변경 필요성, 사업범위, 일정, 품질, 비용 및 계약조건에 미치는 영향을 검토한 결과, "
    "아래와 같이 승인합니다."
)

comparison = hwpers.TableBuilder(4, 3)
comparison.set_header_row(["구 분", "변 경 전", "변 경 후"])
comparison_rows = [
    ["개 발", "사업수행계획서 [   ]쪽\n기존 기능·화면·개발범위 및 일정", "변경요청서 기재 내용 반영\n기능·화면·개발범위 및 일정 확정"],
    ["인 력", "PM: [성명]\n투입MM: [   ]MM", "PM: [성명]\n투입MM: [   ]MM"],
    ["기 간", "기존 일정: [                         ]", "변경 일정: [                         ]"],
]
for r, row in enumerate(comparison_rows, start=1):
    for c, text in enumerate(row):
        comparison.set_cell(r, c, text)
comparison.set_all_borders(hwpers.CellBorderStyle())
w.add_table_with_builder(comparison)

w.add_paragraph("")

# 검토결과
w.add_paragraph_with_bold("[검토결과]")
w.add_paragraph("1. 변경 필요성 및 타당성: □ 적정   □ 보완 필요   □ 부적정")
w.add_paragraph("2. 과업범위 영향: □ 범위 내   □ 범위 조정 필요   □ 계약변경 필요")
w.add_paragraph("3. 사업일정 영향: □ 영향 없음   □ 일정 조정   □ 사업기간 변경 필요")
w.add_paragraph("4. 품질·보안·감리 영향: □ 영향 없음   □ 추가 조치 필요")
w.add_paragraph("5. 사업비 영향: □ 추가 비용 없음   □ 추가 비용 발생(별도 계약변경)")

w.add_paragraph("")
w.add_paragraph_with_bold("[승인결정]")
decision = hwpers.TableBuilder(3, 2)
decision_rows = [
    ["승인구분", "□ 승 인      □ 조건부 승인      □ 불승인"],
    ["승인조건", "[조건부 승인 시 이행조건, 완료기한 및 확인방법을 기재]"],
    ["검토의견", "[변경의 타당성, 일정·품질·비용·계약 영향 및 조치사항을 기재]"],
]
for r, row in enumerate(decision_rows):
    for c, text in enumerate(row):
        decision.set_cell(r, c, text)
decision.set_all_borders(hwpers.CellBorderStyle())
w.add_table_with_builder(decision)

w.add_paragraph("")
w.add_paragraph_with_bold("[승인조건 및 유의사항]")
w.add_paragraph("1. 본 승인사항은 변경승인일 이후부터 적용하며, 승인되지 않은 사항은 기존 사업수행계획서에 따릅니다.")
w.add_paragraph("2. 계약금액, 계약기간 또는 과업범위의 본질적 변경을 수반하는 경우에는 본 승인과 별도로 계약변경 절차를 이행하여야 합니다.")
w.add_paragraph("3. 수급인은 승인된 변경사항을 반영한 사업수행계획서와 관련 산출물을 제출하고, 형상·버전·변경이력을 관리하여야 합니다.")
w.add_paragraph("4. 조건부 승인사항은 지정된 기한 내 이행하고 발주기관의 확인을 받아야 하며, 미이행 시 승인이 철회될 수 있습니다.")

w.add_paragraph("")
w.add_paragraph_with_bold("[비    고]")
w.add_paragraph("1. 별도 추가 비용: □ 없음   □ 있음(금액:                    원)")
w.add_paragraph("2. 첨부서류: 변경요청서 1부, 변경사항을 반영한 사업수행계획서 1부, 관련 검토자료 각 1부.")

w.add_paragraph("")
w.add_aligned_paragraph("위와 같이 사업수행계획서 변경을 승인합니다.", hwpers.ParagraphAlignment.Center)
w.add_aligned_paragraph("2026년      월      일", hwpers.ParagraphAlignment.Center)
w.add_paragraph("")

# 결재/서명란
sign = hwpers.TableBuilder(2, 4)
sign.set_header_row(["구 분", "담 당", "검 토", "승 인"])
sign.set_cell(1, 0, "성명/서명")
sign.set_cell(1, 1, "              (서명)")
sign.set_cell(1, 2, "              (서명)")
sign.set_cell(1, 3, "              (서명)")
sign.set_all_borders(hwpers.CellBorderStyle())
w.add_table_with_builder(sign)

w.add_paragraph("")
w.add_aligned_paragraph("[발 주 기 관 명]", hwpers.ParagraphAlignment.Center)

w.update_statistics()
w.save(str(OUT))
print(OUT)
