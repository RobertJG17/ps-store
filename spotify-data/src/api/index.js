import * as React from 'react';
import SpotifyWebApi from "spotify-web-api-js";
import axios from 'axios';
import qs from 'qs';


// export type Device = {
//     id: string | null;
//     name: string;
//     type:
//       | "Computer"
//       | "Tablet"
//       | "Smartphone"
//       | "Speaker"
//       | "TV"
//       | "AVR"
//       | "STB"
//       | "AudioDongle"
//       | "GameConsole"
//       | "CastVideo"
//       | "CastAudio"
//       | "Automobile"
//       | "Unknown";
//     isActive: boolean;
//     isRestricted: boolean;
//   };


export async function fetchTokenAsync(code) {
  const headers = {
    headers: {
    Accept: 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    }
  };
  const data = {
      grant_type: "authorization_code",
      code: code,
      redirect_uri: 'http://localhost:3000/',
    //   redirect_uri: "exp://ep-rs6.coryortega.react-native.exp.direct:80",
    client_id: '5d228af4d8fe45d5b1bb9702187643c0',
    client_secret: '2e64ed63024a402d81fde645767a3680',
  };

  try {
    const response = await axios.post('https://accounts.spotify.com/api/token', qs.stringify(data), headers)
    return await response;
  } catch (err) {
      console.error(err);
  }
}


export function getCode() {
    const redirect_uri = 'http://localhost:3000/';
    const client_id = '474793580c424c75871ceae58caa9a06';
    const client_secret = '0110454a3aa24e4099e05ce2abfe745a';

    // let scopes = 
    // [
    //     "streaming",
    //     "user-read-currently-playing",
    //     "user-read-playback-state",
    //     "user-library-read",
    //     "user-library-modify",
    //     "user-modify-playback-state",
    //     "user-read-email",
    //     "user-top-read",
    //     "user-read-private",
    //     "playlist-modify-public",
    //     "playlist-modify-private"
    //   ];

      let scopes = "user-top-read"

    window.location.href = 'https://accounts.spotify.com/authorize' +
    '?response_type=code' +
    '&client_id=' + client_id +
    (scopes ? '&scope=' + encodeURIComponent(scopes) : '') +
    '&redirect_uri=' + encodeURIComponent(redirect_uri);

    let search = window.location.search;
    let params = new URLSearchParams(search);
    let foo = params.get('query');
}

export async function fetchRefreshTokenAsync(refreshToken) {
  const headers = {
    headers: {
    Accept: 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    }
  };
  const data = {
      grant_type: "refresh_token",
      refresh_token: refreshToken,
      client_id: '474793580c424c75871ceae58caa9a06',
      client_secret: '0110454a3aa24e4099e05ce2abfe745a',
  };

  try {
    const response = await axios.post('https://accounts.spotify.com/api/token', qs.stringify(data), headers)
    return await response;
  } catch (err) {
      console.error(err);
  }
}

//   export async function fetchDevicesAsync() {
//     const client = await _getClientAsync();
//     const result = await client.getMyDevices();
//     return result.devices
//       .map(
//         (d: typeof result.devices[0]) =>
//           ({
//             id: d.id,
//             name: d.name,
//             isActive: d.is_active,
//             isRestricted: d.is_restricted,
//             type: d.type,
//           } as Device)
//       )
//       .sort((a: Device, b: Device) => (a.isActive && b.isActive ? 0 : -1));
//   }

  export async function playTrackAsync({
    uri,
    // deviceId,
    // time,
  }) {
    const client = await _getClientAsync();
    return await client.play({
      uris: [uri],
      // device_id: deviceId,
      // position_ms: time ?? 0,
    });
  }

//   const stagingUrl = "http://sounddrip-staging2.us-east-1.elasticbeanstalk.com/request"
//   const productionUrl = "http://Sounddrip-prod2.us-east-1.elasticbeanstalk.com/request"

//   export async function postDSSong() {
//     // const token = localStorage.getItem('token');
//     const token = await SecureStore.getItemAsync("token");
//     return axios.post(stagingUrl, {"token": token})
//       .then((res) => {
//         return res.data;
//       })
//       .catch((err) => {
//         console.log(err)
//         return err;
//       })
//   }

  export async function getTracks(trackIds) {
    const client = await _getClientAsync();
    return await client.getTracks([trackIds]);
  }

  export async function pauseAsync() {
    const client = await _getClientAsync();
    return await client.pause();
  }

  export async function getUsersTopTracks() {
    const client = await _getClientAsync();
    return await client.getMyTopTracks({"limit":50});
  }

  export async function getAudioInfo(trackId) {
    const client = await _getClientAsync();
    return client.getAudioFeaturesForTrack(trackId);
  }

  export async function getCurrentPlaybackState() {
    const client = await _getClientAsync();
    return client.getMyCurrentPlaybackState();
  }

  async function _getValidTokenAsync() {
    console.log("getting valid token async...")
    const newToken = await localStorage.getItem("token");
    const lastRefreshed = await localStorage.getItem("tokenTime");
    const refreshToken = await localStorage.getItem("refresh");

    //    const newToken = await localStorage.getItem("token");
    // const lastRefreshed = await localStorage.getItem("tokenTime");
    // const refreshToken = await localStorage.getItem("refresh");

    // const newToken = await SecureStore.getItemAsync("token");
    // const lastRefreshed = await SecureStore.getItemAsync("tokenTime");
    // const refreshToken = await SecureStore.getItemAsync("refresh");

    const currentSeconds = new Date().getTime() / 1000;
    try {
      if (
        //the token expires after 3600 sec, so we check if there's 600
        //seconds left or less, fetch a new token
        currentSeconds > parseInt(lastRefreshed) + 3000
      ) {
        const result = await fetchRefreshTokenAsync(refreshToken);

        //web **wont work on mobile**
        await localStorage.setItem("tokenTime", `${currentSeconds}`);
        await localStorage.setItem("token", result?.data.access_token);
        //ios **wont work on web**
        // await SecureStore.setItemAsync("tokenTime", `${currentSeconds}`);
        // await SecureStore.setItemAsync("token", result?.data.access_token);

        return result?.data.access_token;
      }
    } catch (e) {
      console.log(e);
    }
    return newToken;
  }

  async function _getClientAsync() {
    const token = await _getValidTokenAsync();
    const client = new SpotifyWebApi();
    client.setAccessToken(token);
    return client;
  }
