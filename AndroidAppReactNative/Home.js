
import React, { useState, useEffect, useRef } from 'react';
import { StyleSheet, ImageBackground, Text, View, Button, Platform } from 'react-native';
import Radius from './Radius';

const image = {uri: 'https://uncoveringpa.com/wp-content/uploads/2017/08/Philly-from-South-Street-IMG_0560.jpg'};


export default function Home({route, navigation}) {

 return (
    <View style={styles.container}>
    <ImageBackground source={require('./assets/philly2.jpeg')} resizeMode="cover" style={styles.image}>
      <Button title="Safety Radius" onPress={()=>{
          navigation.navigate('Radius');
          }}/>
          <Text></Text>
        <Button title="About" onPress={()=>{
          navigation.navigate('About');
          }}/>
          <Text></Text>
          <Button title="See something suspicious?" onPress={()=>{
          navigation.navigate('Help');
          }}/>
    </ImageBackground>
  </View>
 );
}
const styles = StyleSheet.create({
    container: {
      flex: 1,
    },
    image: {
      flex: 1,
      justifyContent: 'center',
    },
    text: {
      color: 'white',
      fontSize: 42,
      lineHeight: 84,
      fontWeight: 'bold',
      textAlign: 'center',
      backgroundColor: '#000000c0',
    },
  });
  