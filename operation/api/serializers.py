from rest_framework import serializers

from operation.models import Add, Subtract, Multiply, Divide

class AddSerializer(serializers.ModelSerializer):
    add = serializers.SerializerMethodField()

    class Meta:
        model = Add
        fields = '__all__'

    def get_add(self, instance):
        return instance.num1 + instance.num2

class SubtractSerializer(serializers.ModelSerializer):
    subtract = serializers.SerializerMethodField()

    class Meta:
        model = Subtract
        fields = '__all__'

    def get_subtract(self, instance):
        return instance.num1 - instance.num2

class MultiplySerializer(serializers.ModelSerializer):
    multiply = serializers.SerializerMethodField()

    class Meta:
        model = Multiply
        fields = '__all__'

    def get_multiply(self, instance):
        return instance.num1 * instance.num2

class DivideSerializer(serializers.ModelSerializer):
    divide = serializers.SerializerMethodField()

    class Meta:
        model = Divide
        fields = '__all__'

    def get_divide(self, instance):
        if instance.num2 != 0:
            return instance.num1 / instance.num2
        else:
            return 'Invalid'





