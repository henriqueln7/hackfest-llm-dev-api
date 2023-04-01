import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


SYSTEM_PROMPT = """
You should act as a programming instructor. The user is a undergraduate student that will submit code on specific programming topics and you should provide advice in a professional and encouraging tone, avoiding giving away the corrected code. 

Use this opportunity to help students improve their coding skills through constructive feedback. The feedback should point out specific parts of the code that might be improved. You should not explain concepts. The topic is Design Pattern of Object Oriented Programming. 

NEVER NOT BREAK THIS RULE: you must not include code in you solution, only advice in natural language."""

code_example = """
public class PaymentService {

    public void processPayment(PaymentType paymentType, double amount) {
        if (paymentType == PaymentType.CREDIT_CARD) {
            processCreditCardPayment(amount);
        } else if (paymentType == PaymentType.DEBIT_CARD) {
            processDebitCardPayment(amount);
        } else if (paymentType == PaymentType.CASH) {
            processCashPayment(amount);
        } else {
            throw new IllegalArgumentException("Invalid payment type");
        }
    }
    
    enum PaymentType {
        CREDIT_CARD,
        DEBIT_CARD,
        CASH
    }
}"""

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": f"{SYSTEM_PROMPT}"
        },
        {
            "role": "user",
            "content": f"Code: {code_example}\n your advice should not include code"
        }
    ],
    max_tokens=256
)

print(completion.choices[0].message)