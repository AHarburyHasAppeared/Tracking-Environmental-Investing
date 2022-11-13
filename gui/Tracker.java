/**
gives company information for specific industries, based on user inputs
outputs alternative companies for specific industries
@authors Becky Marcus, Alex Harbury, Fevronia Van Sickle 
@version 11/12/22
*/

import javafx.application.;
import javafx.event.ActionEvent;
import javafx.stage.;
import javafx.scene.;
import javafx.scene.layout.; 
import javafx.scene.control.;
import javafx.scene.input.MouseEvent;
import java.util;
import javafx.scene.control.ScrollBar;


public class Tracker extends Application {

    @Override
    public void start(Stage stage) {

        initUI(stage);
    }

    private void initUI(Stage stage) {

        var root = new StackPane();

        var scene = new Scene(root, 300, 250);

        var lbl = new Label("Simple JavaFX application.");
        lbl.setFont(Font.font("Serif", FontWeight.NORMAL, 20));
        root.getChildren().add(lbl);

        stage.setTitle("Simple application");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}


