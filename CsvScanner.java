import java.util.Scanner;

public class CsvScanner{
  List<List<String>> records = new ArrayList<>();
  public CsvScanner(String fileName){
    
    try (Scanner scanner = new Scanner(new File(fileName));) {
    while (scanner.hasNextLine()) {
        records.add(getRecordFromLine(scanner.nextLine()));
    }
}
    
}
  private List<String> getRecordFromLine(String line) {
    List<String> values = new ArrayList<String>();
    try (Scanner rowScanner = new Scanner(line)) {
        rowScanner.useDelimiter(COMMA_DELIMITER);
        while (rowScanner.hasNext()) {
            values.add(rowScanner.next());
        }
    }
    return values;
  }
}


