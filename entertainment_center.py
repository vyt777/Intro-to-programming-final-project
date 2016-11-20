import media
import cosmic

sun = media.Video('The Sun', 'This is the Sun in HD video', 
'https://www.thesun.co.uk/wp-content/uploads/2016/04/1324311.main_image.jpg?w=768&strip=all',
 'https://www.youtube.com/watch?v=ipvfwPqh3V4')

sunset_on_mars = media.Video('The sunset on Mars', 
'This is how Sun looks from Mars',
'http://www.jpl.nasa.gov/images/msl/20150508b/pia19400-16.jpg',
'https://www.youtube.com/watch?v=aIrEjy54kWQ')

thermonuclear_art = media.Video('Thermonuclear art', 'This is another beautiful video of Sun in HD with cool music. Made by NASA',
'http://i.imgur.com/hsHX7PO.jpg', 'https://www.youtube.com/watch?v=6tmbeLTHC_0&t=120s')

earth = media.Video('The Earth', "Finally the video of Earth.",
'https://i.ytimg.com/vi/oFDeNcu3mnc/maxresdefault.jpg',
'https://www.youtube.com/watch?v=oFDeNcu3mnc')

videos = [sun, sunset_on_mars, thermonuclear_art, earth]
cosmic.open_videos_page(videos)


