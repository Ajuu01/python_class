from django.shortcuts import render

def calculator_view (request):
    context={

    }
    if request.method=="POST":
        form_data=request.POST
        number_a : str = form_data.get("number_a")
        number_b : str = form_data.get("number_b")

        # breakpoint()

        operation=form_data.keys()
        print(f"Number a:{number_a}  Number B:{number_b}, Operaion=>{operation}")

        
    
        if number_a.isnumeric() and number_b.isnumeric():
            #We do Addition Operation
                number_a = float(number_a);
                number_b = float(number_b);
                if "add" in operation:
                    total = number_a + number_b
                    context.update(
                        message = f"Addition of {number_a} and {number_b} is {total}."
                    )
                elif "sub" in operation: 
                    total = number_a - number_b
                    context.update(
                        message = f"Subtraction of {number_a} and {number_b} is {total}."
                    )
                elif "mul" in operation: 
                    total = number_a * number_b
                    context.update(
                        message = f"Multiplication of {number_a} and {number_b} is {total}."
                    )
                elif "div" in operation: 
                    total = number_a / number_b
                    context.update(
                        message = f"Division of {number_a} and {number_b} is {total}."
                )
            
        else:
            #we throw error message stating the exact cause\
            context.update(
                message = "You need to pass numeric values for math operations."
            )
    
    return render(request,"calculator.html",context)