from rest_framework import serializers

from .models import Country, State, City


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name']


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    state = StateSerializer()

    def create(self, validated_data):

        request = self.context['request']

        """state object assignment"""

        state_name = request.data.get('state.name')
        try:
            state = State.objects.get(name=state_name)
        except State.DoesNotExist:
            state = State.objects.create(name=state_name)

        validated_data['state'] = state

        """country object assignment"""

        country_name = request.data.get('country.name')
        try:
            country = Country.objects.get(name=country_name)
        except Country.DoesNotExist:
            country = Country.objects.create(name=country_name)
        validated_data['country'] = country

        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):

        request = self.context['request']

        """state object assignment"""

        state_name = request.data.get('state')
        try:
            state = State.objects.get(name=state_name["name"])
        except State.DoesNotExist:
            state = State.objects.create(name=state_name["name"])

        validated_data['state'] = state

        """country object assignment"""

        country_name = request.data.get('country')
        try:
            country = Country.objects.get(name=country_name["name"])
        except Country.DoesNotExist:
            country = Country.objects.create(name=country_name["name"])
        validated_data['country'] = country

        instance = super().update(instance, validated_data)
        return instance

    class Meta:
        model = City
        fields = ['id', 'city_name', 'pincode', 'state', 'country']
