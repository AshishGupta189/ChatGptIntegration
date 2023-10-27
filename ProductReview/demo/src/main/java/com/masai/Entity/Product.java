package com.masai.Entity;

import java.time.LocalDate;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonIgnore;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import lombok.AllArgsConstructor;
import lombok.Data;

@Entity
@Data
@AllArgsConstructor
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String name;
    private double price;
    private LocalDate cDate;
    private LocalDate uDate;
    
    // Other attributes, getters, setters, and relationships

    public Product() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Product(String name, double price, LocalDate cDate, LocalDate uDate, List<Review> reviews) {
		super();
		this.name = name;
		this.price = price;
		this.cDate = cDate;
		this.uDate = uDate;
		this.reviews = reviews;
	}

	@OneToMany(mappedBy = "product", cascade = CascadeType.ALL,fetch = FetchType.EAGER)
    private List<Review> reviews;
}