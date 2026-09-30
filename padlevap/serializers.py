from rest_framework import serializers
from .models import *  # Replace with your model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = UserAccount
        fields = ('email', 'password')



class InformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id','full_name', 'address_line_1', 'address_line_2', 'city', 'state', 'postalCode', 'countryCode', 'phoneNumber', 'status')



class EmailUserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('email', 'full_name', 'address_line_1', 'address_line_2', 'city', 'state', 'postalCode', 'countryCode', 'phoneNumber')



class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'  # Serialize all fields in the model

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__'  # Serialize all fields in the model


class EmailLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLetter
        fields = '__all__'  # Serialize all fields in the model




class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Serialize all fields in the model


class PostEvSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostEv
        fields = '__all__'  # Serialize all fields in the model



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Serialize all fields in the model





class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'  # Serialize all fields in the model




class ProductImagesVariantionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageVariation
        fields = '__all__'  # Serialize all fields in the model




class SizeVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariation
        fields = '__all__'  # Serialize all fields in the model



class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'  # Serialize all fields in the model



class RviewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RviewsImage
        fields = '__all__'  # Serialize all fields in the model

        

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserAccount.objects.all(), required=False)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), required=False)
    class Meta:
        model = Order
        fields = '__all__'  # Serialize all fields in the model
    
   


class SendEmailForPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmailForPassword
        fields = '__all__'  # Serialize all fields in the model





class SendEmailCreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmailCreateOrder
        fields = '__all__'  # Serialize all fields in the model




class SendEmailTrakingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmailTrakingNumber
        fields = '__all__'  # Serialize all fields in the model




class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = '__all__'  # Serialize all fields in the model




class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'  # Serialize all fields in the model




class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'  # Serialize all fields in the model




class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledEmail
        fields = ['email', 'language', 'name']
