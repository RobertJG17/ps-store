import React, { useState, useEffect } from 'react';
import { getCurrentPlaybackState } from "../api";

function Player() {
    const [song, setSong] = useState(null);
    const [artist, setArtist] = useState(null);
    const [album, setAlbum] = useState(null);
    const [image, setImage] = useState(null);

    useEffect(() => {
        {getCurrentPlaybackState()
          .then(res => {
              console.log(res)
              setSong(res.item.name)
              setArtist(res.item.artists[0].name)
              setAlbum(res.item.album.name)
              setImage(res.item.album.images[1].url)
          })
          .catch(err => console.log(err))
        }
      }, [])

    return (
        <div>
            <img src={image}/>
            <h2>{artist}</h2>
            <h3>{album}</h3>
            <h3>{song}</h3>
        </div>
    )
}

export default Player