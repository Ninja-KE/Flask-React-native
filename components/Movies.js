import React, {useState, useEffect} from 'react'
import {View, Text, FlatList, TouchableOpacity, StyleSheet} from 'react-native'
import axios from 'axios'

const Movies = () => {
    const [movies, setMovies] = useState([])

    useEffect(() => {
        axios.get('http://192.168.137.1:5000/getData')
            .then(res => {
                setMovies(res.data.shows)
            })
    }, [])

    const Item = ({ id, title, category, rating, actor, country }) => (
        <View style={styles.parent}>
            <Text style={styles.text}>{title}</Text>
            <Text style={styles.text}>{category}</Text>
            <Text style={styles.text}>{rating}</Text>
            <Text style={styles.text}>{actor}</Text>
            <Text style={styles.text}>{country}</Text>
        </View>
    )

    const renderItem = ({ item }) => (
        <Item
            id={item.id}
            title={item.title}
            category={item.category}
            rating={item.rating}
            actor={item.actor}
            country={item.country}
        />
    )

    return (
        <FlatList
            data={movies}
            renderItem={renderItem}
            keyExtractor={item => item.id}
        />
    )
}

const styles = StyleSheet.create({
    parent: {
        margin: 10,
        padding: 10,
        borderWidth: 0.2,
        borderRadius: 10
    },
    text: {
        color: 'black'
    }
})

export default Movies