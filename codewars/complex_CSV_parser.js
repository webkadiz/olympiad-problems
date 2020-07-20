class Parser {
  constructor(input, separator, quote) {
    this._input = input;
    this._separator = separator;
    this._quote = quote;
    this._newLine = "\n";
    this._cursorAt = 0;
    this._table = [];
    this._row = [];
    this._fieldType = null;
  }

  parse() {
    while (true) {
      this.detectFieldType();
      const [cursorStart, cursorEnd] = this.findEdges();
      const cutedField = this.cutField(cursorStart, cursorEnd);
      const processedField = this.processField(cutedField);

      this.addFieldToRow(processedField);
      this.toNextPosition();
      this.resetFieldType();

      if (this.endOfInput()) break;
    }

    return this._table;
  }

  endOfInput() {
    return this._cursorAt >= this._input.length;
  }

  detectFieldType() {
    if (this._input[this._cursorAt] === this._quote) {
      this._fieldType = "quote";
    } else {
      this._fieldType = "common";
    }
  }

  findEdges() {
    if (this._fieldType === "quote") return this.findEdgesQuote();
    else if (this._fieldType === "common") return this.findEdgesCommon();
    else throw new Error("wrong field type");
  }

  findEdgesQuote() {
    this._cursorAt++;
    let cursorStart = this._cursorAt;
    let quotesCount = 0;

    while (true) {
      if (this._input[this._cursorAt] === this._quote) {
        this._cursorAt++;
        quotesCount++;

        if (this.endOfInput()) break;
        if (
          (this._input[this._cursorAt] === this._separator ||
            this._input[this._cursorAt] === this._newLine) &&
          quotesCount % 2
        ) {
          break;
        }
        continue;
      }
      this._cursorAt++;
    }

    return [cursorStart, this._cursorAt - 1];
  }

  findEdgesCommon() {
    let cursorStart = this._cursorAt;

    while (true) {
      if (
        this.endOfInput() ||
        this._input[this._cursorAt] === this._separator ||
        this._input[this._cursorAt] === this._newLine
      ) {
        break;
      }

      this._cursorAt++;
    }

    return [cursorStart, this._cursorAt];
  }

  cutField(cursorStart, cursorEnd) {
    return this._input.slice(cursorStart, cursorEnd);
  }

  processField(field) {
    let newField = "";
    let prevChar = null;

    for (const fieldChar of field) {
      if (fieldChar === this._quote && prevChar === this._quote) continue;
      prevChar = fieldChar;
      newField += fieldChar;
    }

    return newField;
  }

  addFieldToRow(field) {
    this._row.push(field);
  }

  toNextPosition() {
    if (this.endOfInput() || this._input[this._cursorAt] === this._newLine) {
      this._table.push(this._row);
      this._row = [];
    }

    this._cursorAt++;
  }

  resetFieldType() {
    this._fieldType = null;
  }
}

function parseCSV(input, separator = ",", quote = '"') {
  const parsedInput = new Parser(input, separator, quote).parse();

  return parsedInput;
}

module.exports = parseCSV;
