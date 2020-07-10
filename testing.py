def test_mp3(path, random_noise=False, random_slice=False, amt=1):

    song_samples = mp3_to_samples(path)
    
        
    if (random_slice):
        index = np.random.random_sample() * (song_samples.shape[0]-2)
        index = round(index)

        
        random = np.random.random_sample()
        
        size_slice = random * (song_samples.shape[0]-index)
        
        
        size_slice = round(size_slice)
        

        
        return(song_samples[index:index+size_slice])

    if (random_noise):
        #add random noise

    """
    turns audio into spectograph

    Parameters
    ----------
    path : str
    string of the mp3 file

    random_noise : boolean
    True if want to apply random noise to function

    random_slice : boolean
    True if we wanr to take a random slice from the song

    Returns
    -------
    
    tranformed song : np.array
    sampled of the song with noise/cut
    
    """

def test_from_mic(time, random_noise, random_slice):

    song_samples = mic_to_samples(time)
