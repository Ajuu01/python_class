from django.shortcuts import render
from Calculator.models import calculator_history

def calculator_view (request):
    context={}
    data={}
    if request.method=="POST":
        form_data=request.POST
        number_a : str = form_data.get("number_a")
        number_b : str = form_data.get("number_b")

        data.update(
             number_a=number_a,
             number_b=number_b
        )
        action=""
        # breakpoint()

        operation=form_data.keys()
        print(f"Number a:{number_a}  Number B:{number_b}, Operaion=>{operation}")

        
    
        if number_a.isnumeric() and number_b.isnumeric():
            #We do Addition Operation
                number_a = float(number_a);
                number_b = float(number_b);
                if "add" in operation:
                    total = number_a + number_b
                    action="Addition"
                    message = f"Addition of {number_a} and {number_b} is {total}."
                    context.update(
                        message = message
                    )
                elif "sub" in operation: 
                    total = number_a - number_b
                    action="Subtraction"
                    message = f"Subtraction of {number_a} and {number_b} is {total}."
                    context.update(
                        message = message
                    )
                elif "mul" in operation: 
                    total = number_a * number_b
                    action="Multiplication"
                    message = f"Multiplication of {number_a} and {number_b} is {total}."
                    context.update(
                        message = message
                    )
                elif "div" in operation: 
                    total = number_a / number_b
                    action="Division"
                    message = f"Division of {number_a} and {number_b} is {total}."
                    context.update(
                        message = message
                    )
                data.update(
                     operation=action,
                     operation_status="Success",
                     result=message
                )
                # instance=calculator_history(**data)
                # instance.save()

                calculator_history.objects.create(**data)
        else:
            #we throw error message stating the exact cause\
            message = "You need to pass numeric values for math operations."

            context.update(
                message = message
            )
    
    return render(request,"calculator.html",context)


    