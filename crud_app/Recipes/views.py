from django.shortcuts import render,redirect
from Recipes.models import *
# Create your views here.
def recipes(request):
    if request.method == "POST":
        data=request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        print(recipe_name)
        print(recipe_description)


        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description =recipe_description,
        )
        return redirect('/recipes/')
    queryset = Recipe.objects.all()
    context = {'recipes' : queryset}

    return render(request, 'recipe.html' , context)

def delete_recipe(request,id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')
def update_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    if request.method =="POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        queryset.save()
        return redirect('/recipes/')
    context  = {'recipe' : queryset}
    return render(request, 'update_recipe.html', context)

