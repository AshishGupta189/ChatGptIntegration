package com.masai.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.masai.Entity.Product;

@Repository
public interface ProductDao extends JpaRepository<Product, Integer>{

}
