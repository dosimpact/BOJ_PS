package main

        import(
            "bufio"
            "fmt"
            "index/suffixarray"
            "os"
            "strconv")

            func getScanner(fp *os.File) *
    bufio.Scanner{
        scanner : = bufio.NewScanner(fp)
                        scanner.Split(bufio.ScanWords)
                            scanner.Buffer(make([] byte, 1000005), 1000005) return scanner
    }

    func getNextString(scanner *bufio.Scanner) string{
        scanner.Scan() return scanner.Text()}

    func getNextInt(scanner *bufio.Scanner) int{
        i,
        _ : = strconv.Atoi(getNextString(scanner)) return i
    }

    func getNextInt64(scanner *bufio.Scanner) int64{
        i,
        _ : = strconv.ParseInt(getNextString(scanner), 10, 64) return i
    }

    func getNextUint64(scanner *bufio.Scanner) uint64{
        i,
        _ : = strconv.ParseUint(getNextString(scanner), 10, 64) return i
    }

    func getNextFloat64(scanner *bufio.Scanner) float64{
        i,
        _ : = strconv.ParseFloat(getNextString(scanner), 64) return i
    }

    func main(){
        fp : = os.Stdin
               wfp :
            = os.Stdout

              scanner :
                = getScanner(fp)
        writer :
            = bufio.NewWriter(wfp)
                  solve(scanner, writer)
                      writer.Flush()
    }

    func solve(scanner *bufio.Scanner, writer *bufio.Writer)
{
n:= getNextInt(scanner)
	var indices = make([]*suffixarray.Index, n)
	for i := 0;
    i < n; i++ {
		str := getNextString(scanner)
		indices[i] = suffixarray.New([]byte(str))
	}
 
	q := getNextInt(scanner)
	for i := 0;
    i < q;
    i++
    {
    str:= getNextString(scanner)
		ans := 0
 
		for j := 0;
        j < n;
        j++
        {
        offsets:
            = indices[j].Lookup([] byte(str), 1) if len (offsets) > 0
            {
                ans++
            }
        }
        fmt.Fprintln(writer, ans)
    }
}