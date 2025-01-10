//DormmateBackendApplication.java
package com.dormmate.dormmate_backend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@ComponentScan
(basePackages = "com.dormmate.dormmatebackend")

@SpringBootApplication
public class DormmateBackendApplication {
	public static void main(String[] args) {
		SpringApplication.run(DormmateBackendApplication.class, args);
	}
}