import React from "react";
import { useState } from 'react';
import { Typography, AppBar,Button,Modal,Box, Card, CardActions, CardContent, CardMedia, CssBaseline, Grid, Toolbar, Container } from '@material-ui/core';
import { PhotoCamera } from "@material-ui/icons";
import useStyles from "./styles"; // to integrate css file 

const App = () => {
    const classes =  useStyles();
    const [cards, setcards] = useState([
        { id: 1, src: 'https://source.unsplash.com/random/?computer', title: "computer", description: "A computer is an electronic device that manipulates information, or data." , hidden: false },
        { id: 2, src: 'https://source.unsplash.com/random/?food', title: "food" , description: "Food is any nutrient-rich material consumed or absorbed by humans, animals, or plants in order to sustain life and growth." , hidden: false },
        { id: 3, src: 'https://source.unsplash.com/random/?class', title: "class" , description: " A group of people sharing the same social, economic, or occupational status"  , hidden: false },
        { id: 4, src: 'https://source.unsplash.com/random/?lion', title: "lion" , description: " Lions have strong, compact bodies and powerful forelegs, teeth and jaws for pulling down and killing prey." , hidden: false },
        { id: 5, src: 'https://source.unsplash.com/random/?media', title: "media" , description: " Media, the plural of medium, broadly describes all channels of communication, including everything from printed paper to digital data."  , hidden: false },
        { id: 6, src: 'https://source.unsplash.com/random/?trees', title: "trees" , description: " A tree is a perennial plant with an elongated stem, or trunk, usually supporting branches and leaves."  , hidden: false }
      ]);
    const [selectedImage, setSelectedImage] = useState('');
    const [selectedTitle, setSelectedTitle] = useState('');
    const [selectedHidden, setSelectedHidden] = useState('');
    const [selectedDescription, setSelectedDescription] = useState('');
    const [open, setOpen] = useState(false);
    
    // function to handle open on click on view button.
    const handleOpen = (imageSrc,imageTitle, description ,hidden) => {
        setSelectedImage(imageSrc);
        setSelectedTitle(imageTitle);
        setSelectedDescription(description);
        setSelectedHidden(hidden);
        setOpen(true);
      };
      
    // function to handle hide and show on click on Hidephoto or Showphoto.
    const handleHideShow = (id) => {
        const updatedCards = cards.map((card) =>
         card.id === id ? { ...card, hidden: !card.hidden } : card
        );
        setcards(updatedCards);
    };


    return(
        <div>
            <>
                <CssBaseline />
                <AppBar position="relative">
                    <Toolbar>
                        <PhotoCamera className={classes.icon}/>
                        <Typography variant="h6">
                            Photo Album
                         </Typography>
                    </Toolbar>

                </AppBar>
                <main>
                    <div className={classes.container}>
                        <Container maxWidth="sm" >  {/* contains different things inside of a specific area of the page */}
                            <Typography variant="h4" align="center" color="textPrimary" gutterBottom> {/* gutterbottom will add margin to the bottom of this Typography */}
                            "Moments in Frames: A Personal Photo Gallery"
                            </Typography>
                            <Typography variant="h6" align="center" color="textSecondary" paragraph>
                            "Moments in Frames" is a handpicked selection of treasured memories. Dive into a visual journey through cherished moments, from family gatherings to breathtaking landscapes. Each image carries a unique story, waiting to be rediscovered. Join us in celebrating the art of photography and the memories it captures
                            </Typography>
                            <div className={classes.button}>
                                <Grid container spacing={2} justifyContent="center">
                                    <Grid item >
                                        <Button variant="contained" color="primary">
                                            see my photos
                                        </Button>
                                    </Grid>
                                    <Grid item >
                                        <Button variant="outlined" color="primary">
                                            secondary action
                                        </Button>
                                    </Grid>
                                </Grid>
                            </div>
                        </Container>
                    </div>
                    <Container className={classes.cardGrid} maxWidth="md">
                        <Grid container spacing={4}>
                            {cards.map((card) => (
                                <Grid item key={card} xs={12} sm={6} md={4}> {/* xs=for mobile devices, sm=for small devices, md=for medium*/}
                                <Card className={classes.card}>
                                    <CardMedia
                                        className={classes.cardMedia}
                                        image={card.hidden ? 'hidden-image.jpg' : card.src}
                                        title={card.title}
                                    />
                                    <CardContent className={classes.cardContent} >
                                        <Typography gutterBottom variant="h5">
                                            {card.title}
                                        </Typography>
                                        <Typography>
                                            {card.description}
                                        </Typography>
                                    </CardContent>
                                    <Modal
                                            hideBackdrop
                                            open={open}
                                            onClose={() => setOpen(false)}
                                            aria-labelledby="modal-modal-title"
                                            aria-describedby="modal-modal-description"
                                            >
                                            <Box className={classes.boxContent} bgcolor='background.paper' boxShadow="24" p="4">
                                                <CardMedia
                                                    className={classes.cardMedia}
                                                    image={selectedHidden ? 'hidden-image.jpg' : selectedImage}
                                                    title={selectedTitle}
                                                />
                                                <CardContent className={classes.cardContent}>
                                                    <Typography gutterBottom variant="h5">
                                                        {selectedTitle}
                                                    </Typography>
                                                    <Typography>
                                                        {selectedDescription}
                                                    </Typography>
                                                </CardContent>
                                            <Button variant="contained" onClick={() => setOpen(false)}>close</Button>
                                            </Box>
                                        </Modal>

                                    <CardActions>
                                        <Button  onClick={() => handleOpen(card.src, card.title, card.description,card.hidden)} size="small" color="primary">view</Button>
                                        
                                        <Button size="small" color="primary" onClick={() => handleHideShow(card.id)}> {card.hidden ? 'Show' : 'Hide'} Photo</Button>
                                    </CardActions>
                                </Card>
                            </Grid>
                            ))}
                            
                        </Grid>

                    </Container>
                </main>
                <footer className={classes.footer}>
                        <Typography variant="h6" align="center" gutterBottom>
                                Footer
                        </Typography>
                        <Typography variant="subtitle1" align="center" color="textSecondary">
                                Thank you for visiting!
                                "© 2023 Moments in Frames. All Rights Reserved. | Privacy Policy | Terms of Use | Contact Us"
                        </Typography>
                </footer>
            </>
        </div>
    );

}
export default App;