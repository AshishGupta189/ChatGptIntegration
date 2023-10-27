package com.masai.Entity;

import java.time.LocalDate;

import com.fasterxml.jackson.annotation.JsonIgnore;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import lombok.Data;

@Entity
@Data
public class Review {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private Integer userId;
    private String description;
    private LocalDate cDate;
    private LocalDate uDate;
    // Other attributes, getters, setters
    	
    @ManyToOne()
    @JoinColumn(name = "product_id")
    @JsonIgnore
    private Product product;
	
    public Review(Integer userId, String description, LocalDate cDate, LocalDate uDate, Product product) {
		super();
		this.userId = userId;
		this.description = description;
		this.cDate = cDate;
		this.uDate = uDate;
		this.product = product;
	}
	public Review() {
		super();
	}
}