package furb;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Rodrigo Fernandes
 */

public class Main {

	public static void main(String[] args) {
		System.out.println(exeProcura.ler());
	}
}

class exeProcura {
	// iInforme o diretório do arquivo aqui
	private static final String LOCAL = "c:\\temp\\entrada.in";
	private static BufferedReader bufferedReader;

	static String ler() {
		int[][] grafo;
		int vertices, arestas;
		String[] aux;
		String saida = "";

		try {
			bufferedReader = new BufferedReader(new FileReader(LOCAL));

			while (bufferedReader.ready()) {
				aux = bufferedReader.readLine().split(" ");
				vertices = Integer.parseInt(aux[0]);
				arestas = Integer.parseInt(aux[1]);

				if (arestas != 0 && vertices != 0) {
					grafo = new int[vertices][vertices]; // Matriz de custo
					for (int j = 0; j < arestas; j++) {
						aux = bufferedReader.readLine().split(" ");
						grafo[Integer.parseInt(aux[0]) - 1][Integer.parseInt(aux[1]) - 1] = Integer.parseInt(aux[2]);
					}
					aux = bufferedReader.readLine().split(" ");
					// Inicializa o grafo e calula a rota
					saida += new Grafo(vertices, grafo).calcularRota(Integer.parseInt(aux[0]), Integer.parseInt(aux[1])) + "\n";
				}
			}

		} catch (FileNotFoundException ex) {
			Logger.getLogger(exeProcura.class.getName()).log(Level.SEVERE, null, ex);
		} catch (IOException ex) {
			Logger.getLogger(exeProcura.class.getName()).log(Level.SEVERE, null, ex);
		}
		return saida;
	}
}
