from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from stock_info import Stock

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

def invesment_report(company, symbol):

    prompt = ChatPromptTemplate.from_messages([
        ("system", """
            Want assistance provided by qualified individuals enabled with experience on understanding charts 
            using technical analysis tools while interpreting macroeconomic environment prevailing across world 
            consequently assisting customers acquire long term advantages requires clear verdicts therefore 
            seeking same through informed predictions written down precisely! First statement contains 
            following content- "Can you tell us what future stock market looks like based upon current conditions ?".
        """),
        ("user", """
            {company} 주식에 투자해도 될까요?
            아래의 기본정보, 재무제표를 참고해 마크다운 형식의 투자보고서를 한글로 작성해 주세여.
        
            기본정보:
            {basic_info}
        
            재무제표:
            {financial_statement}

        """)
    ])

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    stock = Stock(symbol)

    result = chain.invoke({
        "company": company,
        "basic_info": stock.get_basic_info(),
        "financial_statement": stock.get_financial_statement()
    })
    
    return result